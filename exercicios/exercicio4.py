#AULA 51
velocidade = int(input('Digite a velocidade ')) #velocidade do carro
local_carro = int(input('Digite o loacl do carro (KM) ')) #o carro esta no km

RADAR_1 = 60 #velocidade máxima no radar 1
LOCAL_1 = 100 #KM onde esta o radar 1
RADAR_RANGE = 1 #tamanho de alcance do radar

velo_car_1 = velocidade > RADAR_1
passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = velo_car_1 and passou_radar_1

if velo_car_1:
    print(f'Velocidade acima da máxima permitida {RADAR_1}KM!')
if passou_radar_1:
    print('Carrou passou no radar 1')
if carro_multado_radar_1:
    print('Carro multado')