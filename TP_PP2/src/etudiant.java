import javax.xml.bind.annotation.XmlRootElement;
import java.io.Serializable;
@XmlRootElement
public class etudiant implements Serializable {
    private int id;
    private String nom;
    private double moyenne;

    public etudiant(){

    }
    public etudiant(int id, String nom, double moyenne){
        this.id =  id;
        this.nom = nom;
        this.moyenne = moyenne;
    }
    public int getId(){
        return this.id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getNom(){
       return this.nom ;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public double getMoyenne(){
        return this.moyenne;
    }

    public void setMoyenne(double moyenne) {
        this.moyenne = moyenne;
    }
}
