import torch
import model as Model
import argparse
import logging
import core.logger as Logger
import core.metrics as Metrics
from core.wandb_logger import WandbLogger
from tensorboardX import SummaryWriter
import os

from data.util import prepare_testdata

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', type=str, default='config/config.json',
                        help='JSON file for configuration')

    parser.add_argument('-bg', '--bgpath', type=str,
                        default='/root/autodl-tmp/dataset/crack-generate-model/background/IMG_20200105_142819.jpg',
                        help='background img path')
    parser.add_argument('-cp', '--conditionpath', type=str,
                        default='/root/autodl-tmp/dataset/crack-generate-model/condition/IMG_20200105_142542.jpg',
                        help='crack mask img path')
    parser.add_argument('-p', '--phase', type=str, choices=['test'], help='val(generation)', default='test')
    parser.add_argument('-gpu', '--gpu_ids', type=str, default=None)
    parser.add_argument('-debug', '-d', action='store_true')
    parser.add_argument('-enable_wandb', action='store_true')
    parser.add_argument('-log_infer', action='store_true')

    # parse configs
    args = parser.parse_args()
    opt = Logger.parse(args)
    # Convert to NoneDict, which return None for missing key.
    opt = Logger.dict_to_nonedict(opt)

    # logging
    torch.backends.cudnn.enabled = True
    torch.backends.cudnn.benchmark = True

    Logger.setup_logger(None, opt['path']['log'],
                        'train', level=logging.INFO, screen=True)
    Logger.setup_logger('val', opt['path']['log'], 'val', level=logging.INFO)
    logger = logging.getLogger('base')
    logger.info(Logger.dict2str(opt))
    tb_logger = SummaryWriter(log_dir=opt['path']['tb_logger'])

    # model
    diffusion = Model.create_model(opt)
    logger.info('Initial Model Finished')

    diffusion.set_new_noise_schedule(
        opt['model']['beta_schedule']['test'], schedule_phase='test')

    logger.info('Begin Model Inference.')
    current_step = 0
    current_epoch = 0
    idx = 0

    result_path = '{}'.format(opt['path']['results'])
    os.makedirs(result_path, exist_ok=True)

    val_data = prepare_testdata(opt['bgpath'], opt['conditionpath'], opt['datasets']['test']['resolution'])

    diffusion.feed_data(val_data)
    diffusion.test(continous=True)
    visuals = diffusion.get_current_visuals()

    bg_img = Metrics.tensor2img(visuals['bg'])  # uint8
    condition_img = Metrics.tensor2img(visuals['condition'])
    Y0_img = Metrics.tensor2img(visuals['Y0'])  # uint8

    Metrics.save_img(
        Y0_img, '{}/{}_{}_Y0_process.png'.format(result_path, current_step, idx))
    Metrics.save_img(
        Metrics.tensor2img(visuals['Y0'][-1]), '{}/{}_{}_Y0.png'.format(result_path, current_step, idx))
    Metrics.save_img(
        bg_img, '{}/{}_{}_bg.png'.format(result_path, current_step, idx))
    Metrics.save_img(
        condition_img, '{}/{}_{}_condition.png'.format(result_path, current_step, idx))