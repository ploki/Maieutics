from PIL import Image, ImageOps, ImageEnhance, ImageFilter, ImageDraw
import sys, os
HERE=os.path.dirname(os.path.abspath(__file__))
# usage: python3 make_bust.py [columns=22] [gamma=1.4] [background_threshold=45] [--invert]
a=[x for x in sys.argv[1:] if not x.startswith('--')]
cols=int(a[0]) if len(a)>0 else 22; gamma=float(a[1]) if len(a)>1 else 1.4; bg=int(a[2]) if len(a)>2 else 45
inv='--invert' in sys.argv
im=Image.open(os.path.join(HERE,'socrate-anderson-farnese.jpg')).convert('L').crop((70,25,510,625))
im=ImageOps.autocontrast(im,cutoff=1)
im=im.point(lambda p: 0 if p<bg else int(255*((p-bg)/(255-bg))**gamma))
im=im.filter(ImageFilter.UnsharpMask(radius=1.5,percent=120))
w=cols*2; h=int(im.height*w/im.width*1.0); h-=h%4
im=im.resize((w,h),Image.LANCZOS)
if inv: im=ImageOps.invert(im)
bw=im.convert('1'); px=bw.load()
bits=[(0,0,1),(0,1,2),(0,2,4),(1,0,8),(1,1,16),(1,2,32),(0,3,64),(1,3,128)]
lines=[''.join(chr(0x2800+sum(b for dx,dy,b in bits if px[x+dx,y+dy])) for x in range(0,w,2)) for y in range(0,h,4)]
# blank cells (U+2800) become spaces: same picture, far fewer tokens
lines=[l.replace(chr(0x2800),' ').rstrip() for l in lines]
open(os.path.join(HERE,'bust.txt'),'w').write('\n'.join(lines))
# preview: each dot as 3px circle, char cell 2x4 dots, aspect terminal ~ cell w:h=1:2
s=6; prev=Image.new('L',(w*s,h*s),0); d=ImageDraw.Draw(prev)
for y in range(h):
    for x in range(w):
        if px[x,y]: d.ellipse((x*s+1,y*s+1,x*s+s-1,y*s+s-1),fill=255)
prev.save(os.path.join(HERE,'preview.png')); print(len(lines),'rows')
