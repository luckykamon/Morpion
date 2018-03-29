import imageio
import matplotlib.pyplot as plt
import Image
import numpy as np

im = Image.new("RGB", (169,169), "white")
pic = np.array(im)
im=pic
t=85 #rayon du pion
col=-170
lig=170
pioncollig=[0,0] #pion colonne numero puis ligne numero
c=[87+pioncollig[0]*col,87+pioncollig[1]*lig] #centre du pion en bas a gauche
for k in range(169):
  for j in range(169):
    im[k,j] = (156,97,65)
for o in range(-t,t+1):
  for a in range(-t,t+1):
    if o*o+a*a<=t*t:
      if 3600<o*o+a*a<4900:
        im[c[0]+o,c[1]+a] = (20,20,20)
imageio.imsave("round.png", im)

