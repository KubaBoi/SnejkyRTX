Classes:
    Engine 
        init:
            width - sirka Screen
            height - vyska Screen
            Screen (pygame)

        obsahuje:
            Camera
            ObjectManager
            ScreenManager
            LightManager

        metody:
            update()
                updatuje celou scenu
                zavola Camera.update()
                zavola ObjectManager.update()
                zavola LightManager.update()

            draw()
                vykresli celou scenu
                zavola DrawManager.draw()

            addComponent(Component)
                prida Component do
                    - Object -> ObjectManager
                    - Light -> LightManager

            removeComponent(Component)
                odebere Component z 
                    - Object -> ObjectManager
                    - Light -> LightManager

            setCamera(Vector position, Vector direction)
                nastavi Camera

    ObjectManager
     - pracuje s Objecty sceny
        init:
            Engine

        obsahuje:
            objects[] - seznam Object   
            Engine 

        metody:
            updateObjects()
                zavola Object.update() pro cely objects[]

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
            updateLights()
                zavola Light.update() pro cely lights[]

            addLight(Light)
                prida Light do lights[]

            removeLight(Light)
                odeber Light z lights[]  

    ScreenManager
     - Vykresluje obrazovku
     - urcuje jaka data zpracuje jake vlakno

        init:
            Engine
            Screen (pygame)
            width - sirka Screen
            height - vyska Screen

        obsahuje:
            ThreadManager
            Screen
            Engine
            pixelScreen[] - dvojrozmerne pole o velikosti width x height
            width
            height

        metody:
            updateScreen()
                - zavola ThreadManager.update()
                surfarray.blit_array(Screen, pixelScreen[])
                pygame.display.flip()

            drawScreen(int threadIndex, int numberOfPixels)
                - RTX pro cast obrazovky - vystreli paprsky do numberOfPixels pixelu
                - data uklada do pixelScreen[]

    Camera
     - nic nedela, jenom uchovava data o svoji poloze a smeru pohledu

        init:
            Position - Vector
            Direction - Vector

        obsahuje:
            Position
            Direction

        metody:
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
            threadCount

        metody:
            update(int countOfPixels)
                vytvori se nova promenna actTime = time.time()

                - for cyklem se program rozdeli do threadCount vlaken a 
                pro kazde vlakno se zavola (i = <1, threadCount>):
                    ScreenManager.draw(i, countOfPixels/threadCount - zaokrouhleno dolu)

                - pri vytvareni posledniho vlaken:
                    ScreenManager.draw(i, countOfPixels - countOfPixels/threadCount - zaokrouhleno dolu * i-1)
                    aby se projely i zbyvajici pixely

                - pocka az jsou vsechna vlakna hotova
                - actTime = time.time() - actTime

                #pro zacatek bude konstatni pocet vlaken (treba 4)
                pokud je time != 0:
                    pokud je rozdil actTime a time vetsi jak nejaka hodnota