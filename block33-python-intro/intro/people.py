import area


# Utiliza o módulo de cálculo de area para calcular pessoas que estão presentes em um show, dado a área do mesmo.

# Anota aí ✏️: O import é utilizado para termos todas as funções do módulo disponíveis em outro arquivo. Uma outra maneira de utilizarmos é escrevendo from area import rectangle, por exemplo, se quisermos importar apenas rectangle a partir de area. Porém, tome cuidado com conflitos de nomes caso use essa segunda maneira.

PEOPLE_AT_CONCERT_PER_SQUARE_METER = 2  # numero de pessoas por metro quadrado em média
FIELD_LENGTH = 240  # em metros
FIELD_WIDTH = 45  # em metros
PEOPLE_AT_CONCERT = area.rectangle(FIELD_LENGTH, FIELD_WIDTH) // PEOPLE_AT_CONCERT_PER_SQUARE_METER


print("Estão presentes no show aproximadamente", PEOPLE_AT_CONCERT, "pessoas")