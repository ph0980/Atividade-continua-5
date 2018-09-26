from equipe import Equipe

equipe = Equipe()
def test_addIntegrantes():
    assert equipe.adicionarIntegrante('Pedro')==True
    assert equipe.adicionarIntegrante('Ruan')==True
    assert equipe.adicionarIntegrante('Abelardo')==True
    assert equipe.adicionarIntegrante('Lucas')==True
    assert equipe.adicionarIntegrante('Kenny')==True

