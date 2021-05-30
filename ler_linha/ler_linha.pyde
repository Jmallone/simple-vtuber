
def pegaTexto2():
    global y
    with open('/tmp/audio.txt') as f:
        lines = f.readlines()
        print(lines)
        if lines != []:
            num = int(lines[0].split('.')[0])
            print(num)
            y = num
            '''
            if  num > 80 and num < 150:
                print("===========================")
                y += 5
            elif num > 150 and num < 300:
                y += 10
            elif num > 300:
                y += 20
            '''
                
def setup():
  global cima
  global baixo
  global y
  y = 0
  size(500,500)

  cima = loadImage("cima.png")
  baixo = loadImage("baixo.png")

def draw():
  global cima
  global baixo
  global y
  background(255, 204, 0);
  # Draw the image to the screen at coordinate (0,0)
  #y = 0
  pegaTexto2()
  image(cima,0,0)
  
  pushMatrix()
  if y > 200:
    rotate(radians(2))
  elif y > 100:
    translate(0, 20)
    rotate(radians(-4))
  else:
    rotate(radians(0))
    
      
  
  translate(0, 0)
  image(baixo, 5,y%50)
  popMatrix()

    
