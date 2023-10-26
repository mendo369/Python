package logica;

import java.io.Serializable;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

@Entity
public class usuario implements Serializable{
    @Id
    @GeneratedValue (strategy=GenerationType.AUTO)
    private int id;
    private String dni;
    private String name;
    private String lastname;
    private String tel;

    public usuario(int id, String dni, String name, String lastname, String tel) {
        this.id = id;
        this.dni = dni;
        this.name = name;
        this.lastname = lastname;
        this.tel = tel;
    }
    
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getDni() {
        return dni;
    }

    public void setDni(String dni) {
        this.dni = dni;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }

    public String getTel() {
        return tel;
    }

    public void setTel(String tel) {
        this.tel = tel;
    }
    

    public usuario() {
    }

    public usuario(String dni, String name, String lastname, String tel) {
        this.dni = dni;
        this.name = name;
        this.lastname = lastname;
        this.tel = tel;
    }

}
