package com.example.orchestration.drools.vo;


public class Car{

	private String make;
	private String model;
	private int year;
	private String style;
	private String color;
	
	public Car() {}
	
	public Car(String make, String model, int year, String sytle, String color){
		super();
		this.setMake(make);
		this.setModel(model);
		this.setYear(year);
		this.setColor(color);
		this.setStyle(sytle);
	}
	public String getStyle() {
		return style;
	}
	public void setStyle(String style) {
		this.style = style;
	}
	public String getColor() {
		return color;
	}
	public void setColor(String color) {
		this.color = color;
	}
	public String getMake() {
		return make;
	}
	public void setMake(String make) {
		this.make = make;
	}
	public String getModel() {
		return model;
	}
	public void setModel(String model) {
		this.model = model;
	}
	public int getYear() {
		return year;
	}
	public void setYear(int year) {
		this.year = year;
	}
	@Override
	public String toString() {
        return "Car[make=" + make + ",model=" + model + ", year=" + year + ",style=" + style + ",color=" + color + "]";
    }
}

