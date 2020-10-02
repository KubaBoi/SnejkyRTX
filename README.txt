Classes:
    Engine 
        init:
            Screen (pygame)
            width - sirka Screen
            height - vyska Screen
            Camera

        obsahuje:
            Camera
            ObjectManager
            ScreenManager
            LightManager
            Screen (pygame)

        metody:
            update()
                updatuje celou scenu
                zavola Camera.update()
                zavola ObjectManager.update()

            addComponent(Component)
                prida Component do
                    - Object -> ObjectManager
                    - Light -> LightManager

            removeComponent(Component)
                odebere Component z 
                    - Object -> ObjectManager
                    - Light -> LightManager

            setCamera(Vector position, Vector direction)
                zavola Camera.setCamera(position, direction)

    ObjectManager
     - pracuje s Objects sceny
        init:
            Engine

        obsahuje:
            objects[] - seznam Object   
            Engine 

        metody:
            updateObjects()
                zavola Object.update() pro cely objects[]
                seradi objects[] podle vzdalenosti od Engine.Camera
            addObject(Object)
                prida Object do objects[]

            removeObject(Object)
                odeber Object z objects[]     

    LightManager
     - pracuje s Light sceny   
        init:
            Engine

        obsahuje:
            lights[] - seznam Light
            Engine

        metody:
            addLight(Light)
                prida Light do lights[]

            removeLight(Light)
                odeber Light z lights[]  

    ScreenManager
     - Vykresluje obrazovku

        init:
            Engine

        obsahuje:
            ThreadManager
            Engine
	    Screen -> Engine.Screen
            pixelScreen[] - dvojrozmerne pole o velikosti width x height
            width -> Engine.width
            height -> Engine.height

        metody:
            updateScreen()
                - zavola ThreadManager.update()
                surfarray.blit_array(Screen, pixelScreen[])
                pygame.display.flip()

            drawScreen(int threadIndex, int numberOfPixels)
                - RTX pro cast obrazovky - vystreli paprsky do numberOfPixels pixelu
                - data uklada do pixelScreen[]
		

    Camera
        init:
            Position - Vector
            Direction - Vector

        obsahuje:
            Position
            Direction

        metody:
            update()
                zachytava pohyb mysi a upravuje Direction

            setCamera(Vector position, Vector direction)
                pokud jsou location nebo direction None - nezmeni se

    ThreadManager
     - rozdeluje vykreslovani do vlaken
     - dynamicky urcuje kolik vlaken je potreba podle predchozich prubehu

        init:
            ScreenManager - parent

        obsahuje:
            ScreenManager
            time
            threadCount = 4

        metody:
            update(int countOfPixels)
                vytvori se nova promenna actTime = time.time()

                - for cyklem se program rozdeli do threadCount vlaken a 
                pro kazde vlakno se zavola (i = <1, threadCount>):
                    ScreenManager.draw(i, countOfPixels/threadCount - zaokrouhleno dolu)

                - pri vytvareni posledniho vlaken:
                    ScreenManager.draw(i, countOfPixels - (countOfPixels/threadCount - zaokrouhleno dolu) * i-1)
                    aby se projely i zbyvajici pixely

                - pocka az jsou vsechna vlakna hotova
                - actTime = time.time() - actTime

                pokud je time != 0:
                    pokud je actTime mensi nez time -> threadCount++

    ThreadVariables
     - slouzi k uchovavani promennych pro jedno vlakno
    
        init:
            index - index vlakna
            numberOfPixels - pocet pixelu

        obsahuje:
            index
            numberOfPixels
            i - index pro cyklus v drawScreen()