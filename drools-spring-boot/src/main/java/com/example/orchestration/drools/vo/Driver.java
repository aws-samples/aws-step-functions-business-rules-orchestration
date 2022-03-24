package com.example.orchestration.drools.vo;



public class Driver {

	private int age ;
	private String name;

	public Driver() {
		
	}

	public Driver (int age, String name) {
		super();	
		this.age= age;
		this.name = name;	
	}	


	public int getAge() {
		return age;
	}
	public void setAge(int age) {
		this.age = age;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}


	public String toString() {
        return "Driver[age=" + age + ",name=" + name +"]";
    }
	
}

