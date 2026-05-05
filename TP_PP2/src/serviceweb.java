import javax.jws.WebMethod;
import javax.jws.WebParam;
import javax.jws.WebService;
@WebService(targetNamespace ="http://www.univ-spn.fr")

public class serviceweb {
    @WebMethod(operationName = "ConvertirZ")
    public double conv(double mt){
        return mt * 0.2;
    }

    public double sum (@WebParam(name = "param1")  double x, double y) {
        return x+y;
    }

    public etudiant getetudiant(int id){
        return new etudiant(1,"Lilo",15.9);
    }
}
