Classes:
    Engine 
        init:
            width - sirka Screen
            height - vyska Screen

        obsahuje:
            Camera
            ObjectManager
            Screen
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

            setCamera(Vector location, Vector direction)
                nastavi Camera
                pokud jsou location nebo direction None - nezmeni se

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

    

        