package siddhi;

import org.openqa.selenium.By;
import org.junit.Assert;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.Wait;
import org.openqa.selenium.support.ui.WebDriverWait;


public class Health {
	static WebDriver driver;
	static Wait<WebDriver> wait;

	public static void main(String args[]) {
		
		driver = new ChromeDriver();
		//wait = new WebDriverWait(driver, 5);
		
		driver.get("https://hidden-chamber-33381.herokuapp.com/#/");
		Assert.assertEquals("health", driver.getTitle());
		
		driver.manage().window().maximize();
		wait = new WebDriverWait(driver, 3);
		
		driver.findElement(By.xpath("//a[@class = \'alert-link\']")).click();
		wait = new WebDriverWait(driver, 5);
		
		driver.findElement(By.id("username")).sendKeys("admin");
		wait = new WebDriverWait(driver, 3);
		
		driver.findElement(By.id("password")).sendKeys("admin");
		wait = new WebDriverWait(driver, 3);
		
		driver.findElement(By.xpath("//button[@class= \'btn btn-primary\']")).click();
		wait = new WebDriverWait(driver, 3);
		System.out.println("Login Successfull");
		
		wait = new WebDriverWait(driver, 5);
		//driver.close();
	}
	   
}