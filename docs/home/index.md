# Patient Management
[![Issues][issues-shield]][issues-url]

O Projeto consistirá em um sofware gerenciador de ciclo de vida de um paciente dentro de um consultório, envolvendo todas as etapas de uma atendimento, incluindo o início e encerramento do mesmo. 

O software terá como agentes o paciente, o(a) recepcionista, o(a) médico(a) e  o(a) administrador(a).


## Engenharia de requisitos 
 
O presente documento busca , atraves do uso de engenharia de software, em específico com o uso de engenharia de requisitos, elicitar as funcionalidades a serem desenvolvidas no sistema. 

Ao final do presente documento teremos uma visão holística de todo o sistema a ser envolvido, finalizando com uma representação do mesmo por meio de um design de alta fidelidade.

### Diagrama sequencial solto 

Essa diagramação foi desenvolvida de maneira livre, com o intuido de representar possíveis ações gerais do sistema. 
<figure markdown>

![sq_latest](../img/sequencial.png "Sequential Diagram")
</figure>

### Diagrama ER  

O diagrama de entidade-relacionamento representa, por meio de uma abordagem orientada a entidades, os relacionamentos e interações entre essas. 
<figure markdown>

![latest](../img/er_diagram/latest.jpg "Er Diagram")
</figure>
### Diagramas de Casos de uso 

Um diagrama de caso de uso representa uma funcionalidade específica do sistema, mostrando as possibilidades de ações de maneira sequencial. 

#### UC1 – Doctor Flow
<figure markdown>

![uc1_latest](../img/use_cases/requisitos-doctor-latest.png "UC1 Doctor")
</figure>

#### UC2 – Receptionist Flow
<figure markdown>

![uc2_latest](../img/use_cases/requisitos-patient-latest.png "UC2 Receptionist")
</figure>

#### UC3 – Administrador Flow
<figure markdown>

![uc3_latest](../img/use_cases/requisitos-administration-latest.png "UC3 Administration")
</figure>

[issues-shield]: https://img.shields.io/github/issues/devpillow-org/patient-management?style=for-the-badge
[issues-url]: https://github.com/devpillow-org/patient-management/issues