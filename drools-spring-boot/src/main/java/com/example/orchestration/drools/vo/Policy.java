package com.example.orchestration.drools.vo;



public class Policy {
	private int id;
	private double premium;

	
	public Policy() {
		this.id =0;
		this.premium = 0.0;
	}
	public Policy(int id, double premium) {
		super();
		this.id = id;
		this.premium =  premium;
	}
	
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public double getPremium() {
		return premium;
	}
	public void setPremium(double premium) {
		this.premium = premium;
	}
	public void increasePremium(int percent) {
		this.premium = this.premium + (percent * this.premium);
	}
	public String toString() {
        return "Policy[id=" + id + ",premium=" + premium + "]";
    }
	
}
