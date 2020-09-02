filmes  = ["pulp fiction", "scar face", "origens secretas"]
jogos   = ["skyrim", "oblivion", "the last of us", "NFS underground 2"]
livros  = ["A Sútil arte de ligar o f*da-se", "Como fazer amigos e influenciar pessoas", "Harry potter e as reliquias da morte"]
esporte = ["Futebol", "Basquete", "Hockey"]
listatodas = filmes + livros + jogos + esporte
print(listatodas)
for livro in livros:
    print(livro)  #sim, fiz ele mostrar todos
disciplinas = ["Linguagens de programação", "Modelagem de dados"]
listatodas = listatodas + disciplinas