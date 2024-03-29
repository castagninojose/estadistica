hitos = {
    'estimacion puntual': [
        'rao-cramer',
        'rao-blackwell',
    ],
    'intervalos de confianza': [
        'exacto',
        'asintotico',
        'bootstrap',  # NTH
    ],
    'test de hipotesis': [  # TBD
        'unilateral',
        'simetrico',
        'uniformemente mas potente',
    ],
}

"""
    estimacion puntual
    - [ ] rao-cramer
    - [.] rao-blackwell
    intervalos de confianza
    - [ ] exacto
    - [ ] asintotico
    - [ ] bootstrap
    test de hipotesis
    - [ ] unilateral
    - [ ] simetrico
    - [ ] uniformemente mas potente

"""

links_clases = {
    1: [#clase 1 y 2 introducción informal
        'https://drive.google.com/file/d/1MOKoe-aIVB_sxiHebwMr0HwTuQb9goQl/view?usp=sharing',
        'https://drive.google.com/file/d/1PNZGQArB-3fTj8vCjGPq7-W_FOai3sdC/view?usp=sharing',
    ],
    2: [
        'https://drive.google.com/file/d/1HrOUOLMNvTrnKZasT8ffkqHSK_HJKBhf/view?usp=sharing',
        'https://drive.google.com/file/d/1bOKYpBB_J_Wk-FYb9YhU-pkILE_tb4Ug/view?usp=sharing', #estimación no paramétrica de la acumulada
        'https://drive.google.com/file/d/1dp6Lcd6QULIdi-VjCUezc1M9CKIdPlxA/view?usp=sharing', #estimación no paramétrica de la distribución (estimador de parzen)
        'https://drive.google.com/file/d/1edY25yZjLau9_uV-AUI79ri6EzE3N2B-/view?usp=sharing', #tipos de nucleos y estimador de rosenblatt-parzen
    ],
    3: [  #estimacion puntual
        'https://drive.google.com/file/d/1mi2GaamvYuu8j1FWrEkYKfYxQcoPHY37/view?usp=sharing', #metodo de momentos
        'https://drive.google.com/file/d/1ohq6ypf3dPzIu29tZ1oDlTk4qcSOICcI/view?usp=sharing', #metodo de maxima verosimilitud
    ],
    4: [  #estaban al reves
        'https://drive.google.com/file/d/1gORdVoYrrmL6SIg69CrbtYNlX0ZUSM4U/view?usp=sharing', #ejemplos complicados de EMV y atributos a estudiar de un estimador(sesgo, ECM, )
        'https://drive.google.com/file/d/1a_sGYDtFI_pLNgXCcfp3QN3wtcC0Emqn/view?usp=sharing', #sesgo y varianza del estimador de rosenblatt-parzen
    ],
    5: [  #amise y regla de silverman para h, cross validation, introducciona distribucion asintotica y consistencia debil y fuerte
        'https://drive.google.com/file/d/1g4fPgH_-39sFTOIQvvzVxrcNNgpfBKz1/view?usp=sharing'
    ],
    6: [  #estaban desordenados tambien
        'https://drive.google.com/file/d/12B1ZQfCiFB7VoRrGrk_KTtFq5Y_w__Vb/view?usp=sharing', #ecm y consistencia
        'https://drive.google.com/file/d/10uDs10tUxx4kywCiRtfwUtPuVmiC53Vy/view?usp=sharing', 
        'https://drive.google.com/file/d/1G6TX_3PzRAeAqyUCQdiMpsLpX4vJRP-b/view?usp=sharing', #consistencia emv
        'https://drive.google.com/file/d/1eaZl8UTEgofJ7Tbgtku8ei-EU5wdPYJe/view?usp=sharing', # distribucion asintotica emv
    ],
    7: [
        'https://drive.google.com/file/d/1eiaMOt6qs-Zp2AkbjgPwbk-7vN18FRNA/view?usp=sharing', #metodo delta
        'https://drive.google.com/file/d/1a2A6rcRSDWLIq6IcUR_yekx6fmqA4RHI/view?usp=sharing', #intervalos de confianza
    ],
    8: [
        'https://drive.google.com/file/d/13Xp8EaEQ_A3IfnpwylMr1e8tFOJSjZHU/view?usp=sharing', #intervalos exactos bajo normalidad
        'https://drive.google.com/file/d/11yawBVZoN96MyWMKeWtVsaD7ZKC_49Yw/view?usp=sharing',
    ],
    9: ['https://drive.google.com/file/d/18ukanSGHI2QQeeUsceE2-Oi0DIp0z67o/view?usp=sharing'], #mas intervalos bajo normalidad
    10: ['https://drive.google.com/file/d/1vrk6XRbTLQg0B2wPrakAvTmBkINhpi7R/view?usp=sharing'], #intervalos bootstrap
    11: [
        'https://drive.google.com/file/d/1qFjCv5syCSDAjqfcveD3_nZ_P6LVBQ5V/view?usp=sharing', #más intervalos de confianza bootrstrap
        'https://drive.google.com/file/d/18_rhnfIevxb6u1miq13Ut6FIHeRds7rF/view?usp=sharing', #comienza test de hipotesis
    ],
    12: ['https://drive.google.com/file/d/1th_vkKIKmN9DCF8U-4Ilbbb-ve0Kvqw5/view?usp=sharing'], #test de hipotesis
    13: ['https://drive.google.com/file/d/1sNsqIywhA_IrBBULQ-498CQLl0JMTW1P/view?usp=sharing'],
    14: ['https://drive.google.com/file/d/1WfzhsT5zeYyT0tevvxe98i68cHDWRnF9/view?usp=sharing'], #metodo del pivote para el test
    17: [
        'https://drive.google.com/file/d/1PZ_WHF_KsEWQpwE73INnR5kceQITwYqL/view?usp=sharing',
        'https://drive.google.com/file/d/1MyEjxuAGCUZ7zQk9iqTPl0e8mkEEjHfL/view?usp=sharing',
    ],
    18: ['https://drive.google.com/file/d/1_B1dXb27orLN2CIlIhy591awOn-7T6CL/view?usp=sharing'], #modelizacion y prediccion, modelos de regresion
    19: ['https://drive.google.com/file/d/12BHMpXrTxytVlQK3xB3yYHOZlC8BLC6G/view?usp=sharing'], #regresion lineal y cuadrados minimos
    20: [
        'https://drive.google.com/file/d/1QITu7bfJghYY9Mv449uMCmQq1NnUdbfK/view?usp=sharing', #estimador de cuadrados minimos y normal multivariada
        'https://drive.google.com/file/d/1tdHqBrfMb_gooEwlEXHJDnfGMm38DZEx/view?usp=sharing', #normal y cambio de variables con matrices
        'https://drive.google.com/file/d/1yrDKQWeuvi6yBsS0WxFb9eAt3b0Dbs6X/view?usp=sharing', #+ propiedades normal y matrices
        'https://drive.google.com/file/d/1XgfB8gP1-vLTSqDNJ301D-m8jxEgJ9dp/view?usp=sharing', #++ propiedades normal y matrices
        'https://drive.google.com/file/d/1Xs-JYgMxZscGusEJUqTWzJJZewrnEIwI/view?usp=sharing', #relacion entre chi cuadrado y normal multivariada
    ],
    21: [#estaban desordenados tambien
        'https://drive.google.com/file/d/1ZgMArl4EIkyPbqvOAEZxwF-_90EP_33x/view?usp=sharing', #finalizacion y redondeo cuadrados minimos
        'https://drive.google.com/file/d/1exfpf2G1QX-QmT1bd9rElArWtw2e-1vY/view?usp=sharing', #aplicacion en R
    ],
    22: [
        'https://drive.google.com/file/d/1H0QTXQeTYFAqY-igLKBVP-duV0u823Pb/view?usp=sharing', #ejemplo y modelo trade off sesgo varianza
        'https://drive.google.com/file/d/15qCcnhndSrjvKrKXk_cq8pc2hGJg9uvl/view?usp=sharing',
    ],  
    23: ['https://drive.google.com/file/d/1uY6DqE5Y-zm6xzqZ8eznPZBrIFM1Ppvx/view?usp=sharing'], #estimacion no parametrica de la regresion (k-folds?) nucleo de nadaraya watson
    24: ['https://drive.google.com/file/d/1DgV_8H8gVXfSj-y9UAf2XkE63M5gN7R_/view?usp=sharing'], #clasificación (marco teórico y regla de bayes)
}
