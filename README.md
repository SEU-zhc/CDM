# CDM-Crack conditional generative model
Implementation of paper - CDM: Controllable Complex Pavement Crack Conditional Generative Model
![](https://github.com/SEU-zhc/CDM/blob/main/samples/show.png)

## Web Demo
We deployed our model online.
You can generate any crack images using a background image and a crack mask image in [web demo](http://seuzhc.asuscomm.com:44455/). (If encountering unknown errors, please use a mobile device to access.http://seuzhc.asuscomm.com:44455/)

## Installation
```
pip install -r requirement.txt
```
## Testing
Download the [modelfile(skg3)](https://pan.baidu.com/s/1jEvf-uL49U2JxNAnEK0_6w) 

modify the resume_state in config/config.conf

```
python fakeimg.py -bg [backgroundimgpath] -cp [crackimgpath]
```


## More Samples
[More generated crack images(g4jg)](https://pan.baidu.com/s/17iiV2_PzxJae4nwbSjHBhw)
![](https://github.com/SEU-zhc/CDM/blob/main/samples/a.png)
![](https://github.com/SEU-zhc/CDM/blob/main/samples/b.png)
![](https://github.com/SEU-zhc/CDM/blob/main/samples/c.png)
![](https://github.com/SEU-zhc/CDM/blob/main/samples/d.png)

## Training report
Statistical data in training stage are recorded by [wandb](https://wandb.ai/seu_zhc/generate-crack/reports/CDM-training-report--VmlldzoyOTc4NzMw?accessToken=tflfroo4wy9ke894jx0icd1nd9ujd71n1zjdgbf1h7hvn4lyqh6lgyhzen2xeedu)
