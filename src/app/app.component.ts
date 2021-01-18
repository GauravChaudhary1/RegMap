import { Component } from '@angular/core';
import { HttpClient, HttpParams,HttpHeaders} from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app';

  serverData: any;
  employeeData: any;
  employee: any;

  constructor(private httpClient: HttpClient) {
    
  }

  ngOnInit() {
  }

  sayHi() {
    this.httpClient.get('http://127.0.0.1:5000/').subscribe(data => {
      this.serverData = data as JSON;
      console.log(this.serverData);
    })
  }

  getAllEmployees() {
    const opts = { params: new HttpParams({fromString: "_page=1&_limit=10"}) };
    this.httpClient.get('http://127.0.0.1:5000/employees',opts).subscribe(data => {
      this.employeeData = data as JSON;
      console.log(this.employeeData);
    })
  }
  getEmployee() {
    this.httpClient.get('http://127.0.0.1:5000/employees/1').subscribe(data => {
      this.employee = data as JSON;
      console.log(this.employee);
    })
  }
}
