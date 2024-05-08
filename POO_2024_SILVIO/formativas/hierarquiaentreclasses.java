// Classe hierarquiaentreclasses
public class hierarquiaentreclasses {
    private String nome;
    private double salario;
    
    public hierarquiaentreclasses(String nome, double salario) {
        this.nome = nome;
        this.salario = salario;
    }
    
    public void addAumento(double valor) {
        this.salario += valor;
    }
    
    public double ganhoAnual() {
        return this.salario * 12;
    }
    
    public void exibeDados() {
        System.out.println("Nome: " + this.nome);
        System.out.println("Salário: " + this.salario);
    }
    
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public double getSalario() {
        return salario;
    }

    public void setSalario(double salario) {
        this.salario = salario;
    }
}

// Classe Assistente
public class Assistente extends hierarquiaentreclasses {
    private int matricula;

    public Assistente(String nome, double salario, int matricula) {
        super(nome, salario);
        this.matricula = matricula;
    }

    @Override
    public void exibeDados() {
        super.exibeDados();
        System.out.println("Matrícula: " + this.matricula);
    }

    public int getMatricula() {
        return matricula;
    }

    public void setMatricula(int matricula) {
        this.matricula = matricula;
    }
}

// Classe Tecnico
public class Tecnico extends Assistente {
    private double bonus;

    public Tecnico(String nome, double salario, int matricula, double bonus) {
        super(nome, salario, matricula);
        this.bonus = bonus;
    }

    @Override
    public double ganhoAnual() {
        return super.ganhoAnual() + this.bonus;
    }
}

// Classe Administrativo
public class Administrativo extends Assistente {
    private String turno;
    private double adicionalNoturno;

    public Administrativo(String nome, double salario, int matricula, String turno, double adicionalNoturno) {
        super(nome, salario, matricula);
        this.turno = turno;
        this.adicionalNoturno = adicionalNoturno;
    }

    @Override
    public double ganhoAnual() {
        double salarioAnual = super.ganhoAnual();
        if (turno.equalsIgnoreCase("noite")) {
            salarioAnual += (adicionalNoturno * 12);
        }
        return salarioAnual;
    }
}
