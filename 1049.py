animal = {
    'vertebrado' : {
        'ave' : {
            'carnivoro' : 'aguia',
            'onivoro' : 'pomba'
        },
        'mamifero' : {
            'onivoro' : 'homem',
            'herbivoro' : 'vaca'
        }
    },
    'invertebrado' : {
        'inseto' : {
            'hematofogo' : 'pulga',
            'herbivoro' : 'lagarta'
        },
        'anelideo' : {
            'hematofogo' : 'sanguessuga',
            'onivoro' : 'minhoca'
        }
    }
}

entrada1 = input()
entrada2 = input()
entrada3 = input()

saida = animal[entrada1][entrada2][entrada3]

print("{}".format(saida))
