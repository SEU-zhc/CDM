# CDM-Crack conditional generative model
Implementation of paper - CDM: Controllable Complex Pavement Crack Conditional Generative Model

## Web Demo
We deployed our model online.
You can generate any crack images using a background image and a crack mask image in [web demo](http://skingserver.asuscomm.com:44455/).

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

