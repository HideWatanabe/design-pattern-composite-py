# Composite

## Definição do GoF, no livro "Padrões de Projeto" (2000)

### Intenção: 
Compor objetos em estruturas de árvores para representarem hierarquicamente partes-todo. **Composite** permite aos
clientes tratarem de maeira uniforme objetos individuais e composição de objetos.

### Tipo de pattern:
Estrutural

### Também conhecido como:
?

### Aplicável quando:
- Quando quiser representar hierarquias partes-todo de objetos
- Quiser que os clientes sejam capazes de ignorar a diferença entre composições de objetos e objetos individuais. Os
clientes tratarão todos os objetos na estrutura composta de maniera uniforme.

### Participantes:
- **Component:**
    - Declara a interface para os objetos na composição.
    - Implementa comportamento-padrão para a interface comum a todas as classes, conforme apropriado.
    - Declara uma interface para acessar e gerenciar os seus componentes-filhos
    - (opcional) Define uma interface para acessar o pai de um componente na estrutura recursiva e a implementa, se isso
    for apropriado.
- **Leaf:**
    - Representa "objetos-folha" na composição. Uma folha não tem filhos.
    - Define comportamento para objetos primitivos na composição.
- **Composite:**
    - Define comportamento para componentes que tem filhos
    - Armazena os componentes-filhos.
    - Implementa as operações relacionadas com os filhos presentes na interface de **Component**.
- **Client:** Manipula objetos na composição através da interface de **Component**

##