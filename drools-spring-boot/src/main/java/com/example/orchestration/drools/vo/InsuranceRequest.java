package com.example.orchestration.drools.vo;



public class InsuranceRequest {
	

	private Driver driver;
	private Car car;
	private Policy policy;
	
	public InsuranceRequest() {}
	
	public InsuranceRequest(Driver driver, Car car, Policy policy) {
		super();
		this.driver = driver;
		this.car = car;
		this.policy = policy;		
	}
	public Car getCar() {
		return car;
	}
	public void setCar(Car car) {
		this.car = car;
	}
	public Policy getPolicy() {
		return policy;
	}
	public void setPolicy(Policy policy) {
		this.policy = policy;
	}
	public Driver getDriver() {
		return driver;
	}
	public void setDriver(Driver driver) {
		this.driver = driver;
	}
	

	public String toString() {
        return "Driver:" + driver.toString() + "Car:" + car.toString() + "Policy:"+ policy.toString();
    }
	
}
