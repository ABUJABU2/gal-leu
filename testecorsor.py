import random
import time
import os

class Pokemon:
    def __init__(self, nome, tipo, hp, ataque, defesa, ataques):
        self.nome = nome
        self.tipo = tipo
        self.hp_max = hp
        self.hp_atual = hp
        self.ataque = ataque
        self.defesa = defesa
        self.ataques = ataques
        self.nivel = 1
        self.exp = 0
        self.exp_necessaria = 100
    
    def esta_vivo(self):
        return self.hp_atual > 0
    
    def receber_dano(self, dano):
        self.hp_atual = max(0, self.hp_atual - dano)
    
    def curar(self, quantidade):
        self.hp_atual = min(self.hp_max, self.hp_atual + quantidade)
    
    def ganhar_exp(self, quantidade):
        self.exp += quantidade
        if self.exp >= self.exp_necessaria:
            self.subir_nivel()
    
    def subir_nivel(self):
        self.nivel += 1
        self.exp -= self.exp_necessaria
        self.exp_necessaria = int(self.exp_necessaria * 1.2)
        self.hp_max += 10
        self.hp_atual = self.hp_max
        self.ataque += 5
        self.defesa += 3
        print(f"🎉 {self.nome} subiu para o nível {self.nivel}!")
        print(f"HP: {self.hp_max}, Ataque: {self.ataque}, Defesa: {self.defesa}")

class Ataque:
    def __init__(self, nome, poder, tipo, precisao):
        self.nome = nome
        self.poder = poder
        self.tipo = tipo
        self.precisao = precisao

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.equipe = []
        self.pokemon_ativo = None
        self.pokebolas = 10
        self.pocao = 5
        self.dinheiro = 1000
    
    def adicionar_pokemon(self, pokemon):
        if len(self.equipe) < 6:
            self.equipe.append(pokemon)
            if not self.pokemon_ativo:
                self.pokemon_ativo = pokemon
            print(f"✅ {pokemon.nome} foi adicionado à sua equipe!")
        else:
            print("❌ Sua equipe está cheia! Libere um Pokémon primeiro.")
    
    def trocar_pokemon(self):
        if len(self.equipe) <= 1:
            print("❌ Você precisa de pelo menos um Pokémon na equipe!")
            return False
        
        print("\n🔄 Escolha um Pokémon para trocar:")
        for i, pokemon in enumerate(self.equipe):
            status = "⭐ ATIVO" if pokemon == self.pokemon_ativo else ""
            print(f"{i+1}. {pokemon.nome} (Nv.{pokemon.nivel}) - HP: {pokemon.hp_atual}/{pokemon.hp_max} {status}")
        
        try:
            escolha = int(input("Digite o número do Pokémon: ")) - 1
            if 0 <= escolha < len(self.equipe):
                if self.equipe[escolha] == self.pokemon_ativo:
                    print("❌ Este Pokémon já está ativo!")
                    return False
                self.pokemon_ativo = self.equipe[escolha]
                print(f"✅ {self.pokemon_ativo.nome} agora está ativo!")
                return True
            else:
                print("❌ Escolha inválida!")
                return False
        except ValueError:
            print("❌ Digite um número válido!")
            return False

class JogoPokemon:
    def __init__(self):
        self.jogador = None
        self.pokemons_disponiveis = self.criar_pokemons()
        self.areas = self.criar_areas()
        self.area_atual = "Pallet Town"
    
    def criar_pokemons(self):
        pokemons = {
            "Bulbasaur": Pokemon("Bulbasaur", "Planta", 45, 49, 49, [
                Ataque("Investida", 40, "Normal", 100),
                Ataque("Chicote de Vinha", 45, "Planta", 100),
                Ataque("Semente Sanguessuga", 75, "Planta", 100)
            ]),
            "Charmander": Pokemon("Charmander", "Fogo", 39, 52, 43, [
                Ataque("Arranhão", 40, "Normal", 100),
                Ataque("Brasa", 40, "Fogo", 100),
                Ataque("Lança-chamas", 90, "Fogo", 85)
            ]),
            "Squirtle": Pokemon("Squirtle", "Água", 44, 48, 65, [
                Ataque("Tackle", 40, "Normal", 100),
                Ataque("Jato de Água", 40, "Água", 100),
                Ataque("Hidro Bomba", 110, "Água", 80)
            ]),
            "Pikachu": Pokemon("Pikachu", "Elétrico", 35, 55, 40, [
                Ataque("Tackle", 40, "Normal", 100),
                Ataque("Choque do Trovão", 40, "Elétrico", 100),
                Ataque("Trovão", 110, "Elétrico", 70)
            ]),
            "Pidgey": Pokemon("Pidgey", "Voador", 40, 45, 40, [
                Ataque("Tackle", 40, "Normal", 100),
                Ataque("Gust", 40, "Voador", 100),
                Ataque("Ataque Aéreo", 60, "Voador", 100)
            ]),
            "Rattata": Pokemon("Rattata", "Normal", 30, 56, 35, [
                Ataque("Tackle", 40, "Normal", 100),
                Ataque("Mordida", 60, "Normal", 100),
                Ataque("Hiper Raio", 150, "Normal", 90)
            ])
        }
        return pokemons
    
    def criar_areas(self):
        areas = {
            "Pallet Town": {
                "descricao": "Uma pequena cidade pacífica onde sua jornada começa.",
                "pokemons": ["Bulbasaur", "Charmander", "Squirtle"],
                "tipo": "cidade"
            },
            "Route 1": {
                "descricao": "Uma estrada tranquila com grama alta onde Pokémon selvagens aparecem.",
                "pokemons": ["Pidgey", "Rattata"],
                "tipo": "rota"
            },
            "Viridian Forest": {
                "descricao": "Uma floresta densa cheia de Pokémon insetos e plantas.",
                "pokemons": ["Bulbasaur", "Pidgey"],
                "tipo": "floresta"
            }
        }
        return areas
    
    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def mostrar_titulo(self):
        print("=" * 60)
        print("🎮 POKÉMON: A JORNADA COMEÇA! 🎮")
        print("=" * 60)
        print()
    
    def iniciar_jogo(self):
        self.limpar_tela()
        self.mostrar_titulo()
        
        print("🎯 Bem-vindo ao mundo Pokémon!")
        nome_jogador = input("Como você se chama, treinador? ")
        self.jogador = Jogador(nome_jogador)
        
        print(f"\n🌟 Olá, {nome_jogador}! Sua jornada Pokémon está prestes a começar!")
        print("🎁 Você recebeu um Pokémon inicial e alguns itens básicos!")
        
        # Escolha do Pokémon inicial
        self.escolher_pokemon_inicial()
        
        # Tutorial
        self.tutorial()
        
        # Loop principal do jogo
        self.loop_principal()
    
    def escolher_pokemon_inicial(self):
        print("\n🎯 Escolha seu Pokémon inicial:")
        print("1. Bulbasaur (Planta) - HP: 45, Ataque: 49, Defesa: 49")
        print("2. Charmander (Fogo) - HP: 39, Ataque: 52, Defesa: 43")
        print("3. Squirtle (Água) - HP: 44, Ataque: 48, Defesa: 65")
        
        while True:
            try:
                escolha = int(input("Digite sua escolha (1-3): "))
                if escolha == 1:
                    pokemon = self.pokemons_disponiveis["Bulbasaur"]
                    break
                elif escolha == 2:
                    pokemon = self.pokemons_disponiveis["Charmander"]
                    break
                elif escolha == 3:
                    pokemon = self.pokemons_disponiveis["Squirtle"]
                    break
                else:
                    print("❌ Escolha inválida! Digite 1, 2 ou 3.")
            except ValueError:
                print("❌ Digite um número válido!")
        
        self.jogador.adicionar_pokemon(pokemon)
        print(f"🎉 Parabéns! {pokemon.nome} é agora seu parceiro Pokémon!")
    
    def tutorial(self):
        print("\n📚 TUTORIAL:")
        print("• Use 'explorar' para encontrar Pokémon selvagens")
        print("• Use 'equipe' para ver seus Pokémon")
        print("• Use 'itens' para usar itens")
        print("• Use 'mover' para ir para outras áreas")
        print("• Use 'sair' para encerrar o jogo")
        input("\nPressione Enter para continuar...")
    
    def loop_principal(self):
        while True:
            self.limpar_tela()
            self.mostrar_status()
            
            comando = input(f"\n🎯 O que você quer fazer, {self.jogador.nome}? ").lower()
            
            if comando == "explorar":
                self.explorar_area()
            elif comando == "equipe":
                self.mostrar_equipe()
            elif comando == "itens":
                self.mostrar_itens()
            elif comando == "mover":
                self.mover_area()
            elif comando == "sair":
                print("\n👋 Obrigado por jogar! Até a próxima!")
                break
            else:
                print("❌ Comando não reconhecido. Digite 'tutorial' para ver os comandos disponíveis.")
            
            if comando != "sair":
                input("\nPressione Enter para continuar...")
    
    def mostrar_status(self):
        print(f"📍 Área: {self.area_atual}")
        print(f"💰 Dinheiro: ${self.jogador.dinheiro}")
        print(f"🎒 Pokébolas: {self.jogador.pokebolas}")
        print(f"🧪 Poções: {self.jogador.pocao}")
        
        if self.jogador.pokemon_ativo:
            pokemon = self.jogador.pokemon_ativo
            print(f"⭐ Pokémon Ativo: {pokemon.nome} (Nv.{pokemon.nivel})")
            print(f"❤️ HP: {pokemon.hp_atual}/{pokemon.hp_max}")
            print(f"⚔️ Ataque: {pokemon.ataque} | 🛡️ Defesa: {pokemon.defesa}")
    
    def explorar_area(self):
        area = self.areas[self.area_atual]
        
        if area["tipo"] == "cidade":
            print(f"\n🏘️ Você está em {self.area_atual}, uma cidade pacífica.")
            print("Não há Pokémon selvagens aqui. Use 'mover' para ir para uma rota ou floresta.")
            return
        
        print(f"\n🌿 Explorando {self.area_atual}...")
        time.sleep(1)
        
        # Chance de encontrar Pokémon
        if random.random() < 0.7:  # 70% de chance
            pokemon_nome = random.choice(area["pokemons"])
            pokemon_selvagem = self.pokemons_disponiveis[pokemon_nome].__class__(
                pokemon_nome, 
                self.pokemons_disponiveis[pokemon_nome].tipo,
                self.pokemons_disponiveis[pokemon_nome].hp_max,
                self.pokemons_disponiveis[pokemon_nome].ataque,
                self.pokemons_disponiveis[pokemon_nome].defesa,
                self.pokemons_disponiveis[pokemon_nome].ataques
            )
            
            print(f"🐾 Um {pokemon_selvagem.nome} selvagem apareceu!")
            self.batalha_pokemon(pokemon_selvagem)
        else:
            print("🌱 Nenhum Pokémon apareceu desta vez...")
    
    def batalha_pokemon(self, pokemon_selvagem):
        print(f"\n⚔️ INICIANDO BATALHA!")
        print(f"🎯 {self.jogador.pokemon_ativo.nome} vs {pokemon_selvagem.nome}")
        
        while pokemon_selvagem.esta_vivo() and self.jogador.pokemon_ativo.esta_vivo():
            # Turno do jogador
            print(f"\n❤️ Seu {self.jogador.pokemon_ativo.nome}: {self.jogador.pokemon_ativo.hp_atual}/{self.jogador.pokemon_ativo.hp_max}")
            print(f"❤️ {pokemon_selvagem.nome}: {pokemon_selvagem.hp_atual}/{pokemon_selvagem.hp_max}")
            
            print("\n🎯 Escolha sua ação:")
            print("1. Atacar")
            print("2. Usar Poção")
            print("3. Tentar Capturar")
            print("4. Fugir")
            
            try:
                escolha = int(input("Digite sua escolha: "))
                
                if escolha == 1:
                    self.ataque_jogador(pokemon_selvagem)
                elif escolha == 2:
                    self.usar_pocao()
                elif escolha == 3:
                    if self.tentar_capturar(pokemon_selvagem):
                        return
                elif escolha == 4:
                    if self.tentar_fugir():
                        return
                else:
                    print("❌ Escolha inválida! Atacando automaticamente...")
                    self.ataque_jogador(pokemon_selvagem)
                
            except ValueError:
                print("❌ Escolha inválida! Atacando automaticamente...")
                self.ataque_jogador(pokemon_selvagem)
            
            # Verificar se o Pokémon selvagem ainda está vivo
            if not pokemon_selvagem.esta_vivo():
                print(f"🎉 {pokemon_selvagem.nome} foi derrotado!")
                self.jogador.pokemon_ativo.ganhar_exp(50)
                self.jogador.dinheiro += 100
                print(f"💰 Você ganhou $100 e 50 EXP!")
                break
            
            # Turno do Pokémon selvagem
            if pokemon_selvagem.esta_vivo():
                self.ataque_pokemon_selvagem(pokemon_selvagem)
                
                if not self.jogador.pokemon_ativo.esta_vivo():
                    print(f"💀 {self.jogador.pokemon_ativo.nome} foi derrotado!")
                    print("🏥 Você foi levado para o Centro Pokémon...")
                    self.curar_pokemon_derrotado()
                    break
    
    def ataque_jogador(self, pokemon_selvagem):
        pokemon = self.jogador.pokemon_ativo
        
        print(f"\n⚔️ Escolha o ataque de {pokemon.nome}:")
        for i, ataque in enumerate(pokemon.ataques):
            print(f"{i+1}. {ataque.nome} (Poder: {ataque.poder}, Precisão: {ataque.precisao}%)")
        
        try:
            escolha = int(input("Digite o número do ataque: ")) - 1
            if 0 <= escolha < len(pokemon.ataques):
                ataque = pokemon.ataques[escolha]
                
                # Verificar precisão
                if random.randint(1, 100) <= ataque.precisao:
                    # Calcular dano
                    dano = max(1, ataque.poder + pokemon.ataque - pokemon_selvagem.defesa)
                    pokemon_selvagem.receber_dano(dano)
                    
                    print(f"💥 {pokemon.nome} usou {ataque.nome}!")
                    print(f"💥 Causou {dano} de dano em {pokemon_selvagem.nome}!")
                else:
                    print(f"❌ {pokemon.nome} errou o ataque!")
            else:
                print("❌ Escolha inválida! Atacando com o primeiro ataque...")
                self.ataque_jogador(pokemon_selvagem)
        except ValueError:
            print("❌ Escolha inválida! Atacando com o primeiro ataque...")
            self.ataque_jogador(pokemon_selvagem)
    
    def ataque_pokemon_selvagem(self, pokemon_selvagem):
        pokemon = self.jogador.pokemon_ativo
        
        if pokemon_selvagem.ataques:
            ataque = random.choice(pokemon_selvagem.ataques)
            
            # Verificar precisão
            if random.randint(1, 100) <= ataque.precisao:
                # Calcular dano
                dano = max(1, ataque.poder + pokemon_selvagem.ataque - pokemon.defesa)
                pokemon.receber_dano(dano)
                
                print(f"💥 {pokemon_selvagem.nome} usou {ataque.nome}!")
                print(f"💥 Causou {dano} de dano em {pokemon.nome}!")
            else:
                print(f"❌ {pokemon_selvagem.nome} errou o ataque!")
    
    def usar_pocao(self):
        if self.jogador.pocao > 0:
            pokemon = self.jogador.pokemon_ativo
            cura = 50
            pokemon.curar(cura)
            self.jogador.pocao -= 1
            print(f"🧪 {pokemon.nome} usou uma poção e recuperou {cura} HP!")
            print(f"🧪 Poções restantes: {self.jogador.pocao}")
        else:
            print("❌ Você não tem poções!")
    
    def tentar_capturar(self, pokemon_selvagem):
        if self.jogador.pokebolas > 0:
            print(f"🎯 Tentando capturar {pokemon_selvagem.nome}...")
            time.sleep(1)
            
            # Chance de captura baseada no HP restante
            hp_percentual = pokemon_selvagem.hp_atual / pokemon_selvagem.hp_max
            chance_captura = (1 - hp_percentual) * 0.8  # Máximo 80% de chance
            
            if random.random() < chance_captura:
                print(f"🎉 {pokemon_selvagem.nome} foi capturado com sucesso!")
                self.jogador.adicionar_pokemon(pokemon_selvagem)
                self.jogador.pokebolas -= 1
                return True
            else:
                print(f"❌ {pokemon_selvagem.nome} quebrou a Pokébola!")
                self.jogador.pokebolas -= 1
                return False
        else:
            print("❌ Você não tem Pokébolas!")
            return False
    
    def tentar_fugir(self):
        chance_fuga = 0.5  # 50% de chance
        if random.random() < chance_fuga:
            print("🏃 Você conseguiu fugir da batalha!")
            return True
        else:
            print("❌ Não conseguiu fugir!")
            return False
    
    def curar_pokemon_derrotado(self):
        for pokemon in self.jogador.equipe:
            pokemon.hp_atual = pokemon.hp_max
        print("💚 Todos os seus Pokémon foram curados!")
    
    def mostrar_equipe(self):
        print(f"\n👥 EQUIPE DE {self.jogador.nome.upper()}:")
        if not self.jogador.equipe:
            print("❌ Você não tem Pokémon na equipe!")
            return
        
        for i, pokemon in enumerate(self.jogador.equipe):
            status = "⭐ ATIVO" if pokemon == self.jogador.pokemon_ativo else ""
            print(f"{i+1}. {pokemon.nome} (Nv.{pokemon.nivel}) - {pokemon.tipo}")
            print(f"   ❤️ HP: {pokemon.hp_atual}/{pokemon.hp_max}")
            print(f"   ⚔️ Ataque: {pokemon.ataque} | 🛡️ Defesa: {pokemon.defesa}")
            print(f"   📊 EXP: {pokemon.exp}/{pokemon.exp_necessaria}")
            print(f"   {status}")
            print()
        
        if len(self.jogador.equipe) > 1:
            trocar = input("Deseja trocar o Pokémon ativo? (s/n): ").lower()
            if trocar == 's':
                self.jogador.trocar_pokemon()
    
    def mostrar_itens(self):
        print(f"\n🎒 INVENTÁRIO DE {self.jogador.nome.upper()}:")
        print(f"🎯 Pokébolas: {self.jogador.pokebolas}")
        print(f"🧪 Poções: {self.jogador.pocao}")
        print(f"💰 Dinheiro: ${self.jogador.dinheiro}")
        
        if self.jogador.pocao > 0:
            usar = input("Deseja usar uma poção no Pokémon ativo? (s/n): ").lower()
            if usar == 's':
                self.usar_pocao()
    
    def mover_area(self):
        print(f"\n🗺️ ÁREAS DISPONÍVEIS:")
        areas = list(self.areas.keys())
        for i, area in enumerate(areas):
            descricao = self.areas[area]["descricao"]
            print(f"{i+1}. {area}: {descricao}")
        
        try:
            escolha = int(input("Para qual área você quer ir? ")) - 1
            if 0 <= escolha < len(areas):
                nova_area = areas[escolha]
                if nova_area != self.area_atual:
                    print(f"🚶 Movendo para {nova_area}...")
                    time.sleep(1)
                    self.area_atual = nova_area
                    print(f"✅ Você chegou em {nova_area}!")
                else:
                    print("❌ Você já está nesta área!")
            else:
                print("❌ Escolha inválida!")
        except ValueError:
            print("❌ Digite um número válido!")

def main():
    jogo = JogoPokemon()
    jogo.iniciar_jogo()

if __name__ == "__main__":
    main()