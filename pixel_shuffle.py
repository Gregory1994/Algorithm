import numpy as np
def subpixel_downsample(x,downscale=2):
    n,c,h,w = x.shape
    s = downscale
    if h%s != 0 or w%s != 0:
        print('!!!!Notice: the image size can not be downscaled by current scale')
        exit()
    x = np.reshape(x, [n, c, h // s, s, w // s, s])
    x = np.transpose(x, [0, 1, 3, 5, 2, 4])
    x = np.reshape(x, [n, s * s * c, h // s, w // s])
    return x

def subpixel_upsample(x,upscale=2):
    n,c,h,w = x.shape
    s = upscale
    if c%s != 0:
        print('!!!!Notice: current channel can not be upscale')
        exit()
    x = np.reshape(x,[n,c//(s**2),s,s,h,w])
    x = np.transpose(x,[0,1,4,2,5,3])
    x = np.reshape(x,[n,c//(s**2),h*s,w*s])
    return x
    
if __name__=='__main__':
    a = np.array([[i+j*6 for i in range(6)] for j in range(6)])
    a = a.reshape(1,1,6,6)
    b = subpixel_downsample(a,2)
    c = subpixel_upsample(b,2)
    print(a)
    print(b)
    print(c)