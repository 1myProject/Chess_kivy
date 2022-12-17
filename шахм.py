from kivy.app                     import App
from kivy.uix.gridlayout   import GridLayout
from kivy.uix.boxlayout   import BoxLayout
from kivy.uix.button         import Button
from kivy.uix.label            import Label
from kivy.uix.modalview import ModalView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.pagelayout import PageLayout

from math import fabs

try:
    import s 
except:
    ss=open('s.py','w')
    ss.write('bts=[]')
    ss.close()
    import s
'''
2)красивые переходы
'''
    
class ches (App):
    
    #ходы--------------------------------------------------------------
    def hod(self,ev):
        #self.lb.text=str(c)
        
        self.mojno=True
        if ev.background_normal[6:8]!='фо':
            try:
                even=ev.background_normal[7]
                ev0=ev.background_normal[6]
            except:
                even=''
                ev0=''
        else:
            even=''
            ev0=''
        
        c=self.bts.index(ev)
        
        if self.najat:
            if self.kto:
                if ev0!='w': self.mojno=False
            else:
                if ev0!='b': self.mojno=False
        else:
            if even=='':
                if ev.background_color==[1,1,1,1]:self.mojno=False
            elif ev0==self.figur[0]:
                if ev.background_color == [1,1,0,1]:
                    pass
                elif c!=self.m_figur:
                    self.mojno=False
            else:
                if ev.background_color!=[1,0,0,1]:self.mojno=False
            
        bs=lambda x: self.bts[x].background_normal
        b6=lambda x: self.bts[x].background_normal[6]
        b7=lambda x: self.bts[x].background_normal[7]
        pust=lambda x: self.puty.format(self.papk,'фон',self.bts[x].text[0])
        
        #если всё
        if self.win: self.mojno=False
        
        if self.mojno:
            if self.najat:
                
                if even in ['B','R','Q']:#сллн|ладья|королева
                    self.prov(c)
                    for z in self.lks(even):
                        f=True if z==-1 or z==7 or z==-9 else False
                        t=64 if z>0 else -1
                        if fabs(z)==8: f=None
                        for i in range(c+z,t,z):
                            if f: 
                                if i%8==7: break    
                            elif f==False:
                                if i%8==0: break
                            if bs(i) == pust(i) :
                                self.bts[i].background_color=(0,1,0,1)
                                self.bts[i].background_normal=''
                            elif b6(i)==ev0:break
                            elif b6(i) != ev0:
                                self.bts[i].background_color=(1,0,0,1)
                                break
                
                elif even=='P':#пешка
                    self.najat=False
                    p=False
                    if ev0=='w':
                        if c//8==6:p=True
                        if b6(c-8)!='ф':p=False
                        g,f,d,d1=c-7,c-9,c-8,c-16
                    else:
                        if c//8==1:p=True
                        if b6(c+8)!='ф':p=False
                        f,g,d,d1=c+7,c+9,c+8,c+16
                    if c%8!=0:
                        if bs(f) == pust(f): pass
                        elif b6(f) != ev0:
                            self.bts[f].background_color=(1,0,0,1)
                    if c%8!=7:
                        if bs(g) == pust(g) : pass
                        elif b6(g) != ev0:
                            self.bts[g].background_color=(1,0,0,1)
                    if bs(d) == pust(d) :
                        self.bts[d].background_color=(0,1,0,1)
                        self.bts[d].background_normal=''
                    if p:
                        if b6(d1)=='ф':
                            self.bts[d1].background_color=(0,1,0,1)
                            self.bts[d1].background_normal=''
                        else:
                            self.bts[d1].background_color=(1,0,0,1)
                    
                elif even in ['N','K'] :#лошадь|король
                    self.najat=False
                    self.prov(c)
                    for i in self.lk(c,even):
                        if i<0: continue
                        try:
                            if bs(i) == pust(i):
                                self.bts[i].background_color=(0,1,0,1)
                                self.bts[i].background_normal=''
                            elif b6(i) != ev0:
                                self.bts[i].background_color=(1,0,0,1)
                        except: continue
                self.m_figur=c
                self.figur=ev.background_normal[6:8]
                
            else:#шаг
                pust1=lambda x: self.puty.format(self.papk,'фон',x)
                if c==self.m_figur:
                    for i in self.bts:
                        if i.background_color==[0,1,0,1]:
                            i.background_normal=pust1(i.text[0])
                        i.background_color=(1,1,1,1)
                    self.najat=True
                else:
                    self.kto=not self.kto
                if ev.background_color==[0,1,0,1] or ev.background_color==[1,0,0,1]:
                    for i in self.bts:
                        if i.background_color==[0,1,0,1]:
                            i.background_normal=pust1(i.text[0])
                        i.background_color=(1,1,1,1)
                        
                    s=ev.text[0]
                    ev.background_normal=self.puty.format(self.papk,self.figur,s)
                    s=self.bts[self.m_figur].text[0]
                    self.bts[self.m_figur].text=s+'2'
                    self.bts[self.m_figur].background_normal=self.puty.format(self.papk,'фон',s)
                    self.najat=True
                    
                    #превращение
                    for i in range(8):
                        if b7(i) == 'p':self.bts[i].background_normal=self.puty.format(self.papk,self.img1[3],self.bts[i].text[0])
                    for i in range(56,64):
                        if b7(i) == 'p':self.bts[i].background_normal=self.puty.format(self.papk, self.img2[3],self.bts[i].text[0])
                #ракеровка
                elif ev.background_color==[1,1,0,1]:
                    if even=='K':
                        if self.bts[c+1].background_color == [0,1,0,1]:
                            sp=[c,c+3]
                            sp1=[]
                            for i in self.bts:
                                if i.background_color==[0,1,0,1]:
                                    i.background_normal=pust1(i.text[0])
                                i.background_color=(1,1,1,1)
                            for i in sp:
                                sp1.append(self.bts[i].background_normal[6:8])
                                self.bts[i].text=self.bts[i].text[0]+'2'
                                self.bts[i].background_normal=pust(i)
                            self.bts[c+1].background_normal=self.puty.format(self.papk,sp1[1],self.bts[c+1].text[0])
                            self.bts[c+2].background_normal=self.puty.format(self.papk,sp1[0],self.bts[c+2].text[0])
                        elif self.bts[c-1].background_color==[0,1,0,1]:
                            sp=[c,c-4]
                            sp1=[]
                            for i in self.bts:
                                if i.background_color==[0,1,0,1]:
                                    i.background_normal=pust1(i.text[0])
                                i.background_color=(1,1,1,1)
                            for i in sp:
                                sp1.append(self.bts[i].background_normal[6:8])
                                self.bts[i].text=self.bts[i].text[0]+'2'
                                self.bts[i].background_normal=pust(i)
                            self.bts[c-2].background_normal=self.puty.format(self.papk,sp1[1],self.bts[c-2].text[0])
                            self.bts[c-3].background_normal=self.puty.format(self.papk,sp1[0],self.bts[c-3].text[0])
                    elif even=='R':
                        if c==63 or c==7:
                            sp=[c,c-3]
                            sp1=[]
                            for i in self.bts:
                                if i.background_color==[0,1,0,1]:
                                    i.background_normal=pust1(i.text[0])
                                i.background_color=(1,1,1,1)
                            for i in sp:
                                sp1.append(self.bts[i].background_normal[6:8])
                                self.bts[i].text=self.bts[i].text[0]+'2'
                                self.bts[i].background_normal=pust(i)
                            self.bts[c-1].background_normal=self.puty.format(self.papk,sp1[1],self.bts[c-1].text[0])
                            self.bts[c-2].background_normal=self.puty.format(self.papk,sp1[0],self.bts[c-2].text[0])
                        
                        elif c==56 or c==0:
                            sp=[c,c+4]
                            sp1=[]
                            for i in self.bts:
                                if i.background_color==[0,1,0,1]:
                                    i.background_normal=pust1(i.text[0])
                                i.background_color=(1,1,1,1)
                            for i in sp:
                                sp1.append(self.bts[i].background_normal[6:8])
                                self.bts[i].text=self.bts[i].text[0]+'2'
                                self.bts[i].background_normal=pust(i)
                            self.bts[c+1].background_normal=self.puty.format(self.papk,sp1[0],self.bts[c+1].text[0])
                            self.bts[c+2].background_normal=self.puty.format(self.papk,sp1[1],self.bts[c+2].text[0])
                
                with open("s.py","w") as ss:
                    b=[]
                    for i in range(64):
                        b.append(self.bts[i].background_normal)
                    ss.write('bts={}'.format(list(b)))

            #проверка на выйгрыш
            ch=0#обнуление
            for i in self.bts:
                if i.background_normal[6:8] =='bK':ch+=1
                elif i.background_normal[6:8] =='wK':ch+=2
            if ch==1 or ch==2:
                self.win=True
                v='выйграло\nкоролевство\nчерных' if ch==1 else 'выйграло\nкоролевство\nбелых'
                mv=ModalView(auto_dismiss=True,size_hint=(1,.25))
                mv.add_widget(Label(text=v,font_size='180',))
                mv.open()
                self.fl.add_widget(self.but)
                with open('s.py','w') as ss:
                    ss.write('bts=[]')
        
        #проверка на цвет
        for i in self.bts:
            if i.background_color ==[1,1,1,1]:self.najat=True
            else:
                self.najat=False
                break
    
    
#-----------------------------------------------------------------------------------
#постройка------------------------------------------------------------------
#-----------------------------------------------------------------------------------
    def build(self):
        self.najat=True
        self.kto=True
        self.mojno=True
        self.win=False
        self.puty='{}/{}{}.png'
        self.papk='pixel'
        self.gg=''
        self.figur=''
        self.m_figur=0
        self.bts=[]
        self.img1=[
        'wR',#0 лодья
        'wB',#1 слон
        'wN',#2 лошадь
        'wQ',#3 королева
        'wK',#4 король
        'wP'#5 пешка
        ]
        self.img2=[
        'bR',#0
        'bB',#1
        'bN',#2
        'bK',#3
        'bQ',#4
        'bP'#5
        ]
#-----------------------------------------------------------------------------------
        self.gl=GridLayout(cols=8,rows=8,spacing=1)
        self.gl.bind(size=self.upd)
        self.fl=FloatLayout()
#-----------------------------------------------------------------------------------
        self.lb=Label(size_hint=(1,.2))
        self.but=Button(on_press=self.res,text='заново',font_size='100')
        self.fl.add_widget(self.but)
        self.fl.add_widget(self.gl)
        self.fl.add_widget(self.lb)
        
        #создание поля
        self.pol()
        
        #цвет и фигуры
        self.fig1()
#-----------------------------------------------------------------------------------
#        for i in range(64):
#            s=self.bts[i].text[0]
#            ss='фон'
#            self.bts[i].background_normal= self.puty.format(ss,s)
#        self.bts[60].background_normal=self.puty.format(self.img1[4],'')
#        self.bts[4].background_normal=self.puty.format(self.img2[3],'')

#        r=56
#        self.bts[r].background_normal=self.puty.format(self.img1[0],self.bts[r].text[0])
#-----------------------------------------------------------------------------------
        return self.fl

#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
    
    def prov(self,f):
        sp=[0,4,7,56,60,63]
        if f in sp:
            if self.bts[f].text[1]=='1':
                sp=[[[0,4],[56,60]],[[7,4],[63,60]]]
                bs=lambda x: self.bts[x].background_normal
                pust=lambda x: self.puty.format(self.papk,'фон',self.bts[x].text[0])
                bt=lambda x: self.bts[x].text[1]
                racer=True
                racer1=True
                if f in sp[0][0]:
                    ch=0
                    for i in (1,2,3):
                        if bs(i) != pust(i):racer=False 
                elif f in sp[0][1]:
                    ch=0
                    for i in (57,58,59):
                        if bs(i) != pust(i):racer=False
                if f in sp[1][0]:
                    ch=0
                    for i in (5,6):
                        if bs(i) != pust(i):racer1=False
                elif f in sp[1][1]:
                    ch=0
                    for i in (61,62):
                        if bs(i) != pust(i):racer1=False 
                if racer:
                    if f==4:
                        if bt(0)=='1':self.bts[0].background_color=(1,1,0,1)
                    elif f==0:
                        if bt(4)=='1':self.bts[4].background_color=(1,1,0,1)
                    elif f==56:
                        if bt(60)=='1':self.bts[60].background_color=(1,1,0,1)
                    elif f==60:
                        if bt(56)=='1':self.bts[56].background_color=(1,1,0,1)
                if racer1:
                    if f==7:
                        if bt(4)=='1':self.bts[4].background_color=(1,1,0,1)
                    elif f==63:
                        if bt(60)=='1':self.bts[60].background_color=(1,1,0,1)
                    elif f==4:
                        if bt(7)=='1':self.bts[7].background_color=(1,1,0,1)
                    elif f==60:
                        if bt(63)=='1':self.bts[63].background_color=(1,1,0,1)
    
    def lk(self,f,ff):
        if ff=='K':
            if f%8==0:sp=[f-8,f+8,f-7,f+1,f+9,]
            elif f%8==7:sp=[f-9,f-1,f+7,f-8,f+8,]
            else:sp=[f-9,f-1,f+7,f-8,f+8,f-7,f+1,f+9,]
        else:
            if f%8==0:sp=[f-15,f+17,f-6,f+10,]
            elif f%8==1:sp=[f-17,f+15,f-15,f+17,f-6,f+10,]
            elif f%8==6:sp=[f-10,f+6,f-17,f+15,f-15,f+17,]
            elif f%8==7:sp=[f-10,f+6,f-17,f+15,]
            else:sp=[f-10,f+6,f-17,f+15,f-15,f+17,f-6,f+10,]
        return sp
        
    
    def lks(self,ff):
        if ff=='B': return [7,9,-7,-9]
        elif ff=='R':return [1,8,-1,-8]
        else:return [7,9,-7,-9,1,8,-1,-8]
            
    def upd(self,*arg):
        if self.gl.size[1] > self.gl.size[0]:
            h=(self.gl.size[1] - self.gl.size[0])//2
            self.gl.padding=[0,h]
            self.but.size_hint=(1,h/self.gl.size[1])
        else:
            h=(self.gl.size[0] - self.gl.size[1])//2
            self.gl.padding=[h,0]
            self.but.size_hint=(h/self.gl.size[0],1)
    
    def res(self,ev):
        #self.fl.remove_widget(self.but)
        self.win=False
        self.kto=True
        self.fig()
        with open('s.py','w') as ss:
            ss.write('bts=[]')
    
    #поле==================    
    def pol(self):
        for i in range(64):
            f=True if i//8&1==0 else False
            if f:v='1' if i%8&1==0 else '0'
            else:v='0' if i%8&1==0 else '1'
            
            bt=Button(text=v,color=(1,0,0,1),background_normal='',on_press=self.hod)
            self.gl.add_widget(bt)
            self.bts.append(bt)
            
        sp=[0,4,7,56,60,63]
        for i in range(64):
            if i in sp:self.bts[i].text+='1'
    
    #расстановка фигур
    def fig(self):
        sp=[0,1,2,4,3,2,1,0,5,5,5,5,5,5,5,5]
        r=0
        for i in sp:
            s=self.bts[r].text[0]
            ss=self.img2[i]
            self.bts[r].background_normal= self.puty.format(self.papk,ss,s)
            r+=1
        for i in range(32):
            s=self.bts[r+i].text[0]
            ss='фон'
            self.bts[r+i].background_normal= self.puty.format(self.papk,ss,s)
        r=1
        for i in sp:
            s=self.bts[-r].text[0]
            ss=self.img1[i]
            self.bts[-r].background_normal=self.puty.format(self.papk,ss,s)
            r+=1
            
    def fig1(self):
        if s.bts!=[]:
            for i in range(64):
                self.bts[i].background_normal=s.bts[i]
        else:
            self.fig()

ches().run()