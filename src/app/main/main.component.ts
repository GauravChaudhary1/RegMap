import { Component, OnInit } from '@angular/core';
import { FormModule, ButtonModule } from '@fundamental-ngx/core';
import { HttpClient, HttpParams,HttpHeaders} from '@angular/common/http';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  tableRows: any[] | undefined;
  query: string = '';
  constructor(private httpClient: HttpClient) { }

  ngOnInit(): void {

  }


  onSearch(){
    let qStr = 'qStr=' + this.query;
    const opts = { params: new HttpParams({fromString: qStr}) };
    this.httpClient.get('http://127.0.0.1:5000/',opts).subscribe(data  => {
      let s = data as string;
      let d = JSON.parse(s);
      this.tableRows = Array.of(d)[0];
      console.log(this.query)
    })
  }
}
