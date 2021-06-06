import PyATEMMax
switcher = PyATEMMax.ATEMMax()

try:

    #Conectar com a placa
    switcher.connect("192.168.1.111")
    switcher.waitForConnection()

    #Teste de métocos para troca de tela
    switcher.setAudioMixerMasterVolume(1.8)
    switcher.setPreviewInputVideoSource(0, 5)

    switcher.disconnect()

except ValueError:
    print('Erro ao tentar executar o comando, mensagem: '.format(ValueError))
