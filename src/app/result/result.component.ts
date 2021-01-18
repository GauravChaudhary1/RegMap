import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-result',
  templateUrl: './result.component.html',
  styleUrls: ['./result.component.css']
})
export class ResultComponent implements OnInit {
  tableRows: any[] | undefined;
  constructor() { }

  ngOnInit(): void {
    this.tableRows = [
        {
            column1: 'user.name@email.com',
            column2: 'Row 1',
            column3: 'Row 1',
            date: '09-07-18',
            type: 'accept'
        },
        {
            column1: 'user.name@email.com',
            column2: 'Row 2',
            column3: 'Row 2',
            date: '09-08-18',
            type: 'decline'
        },
        {
            column1: 'user.name@email.com',
            column2: 'Row 3',
            column3: 'Row 3',
            date: '02-14-18',
            type: 'decline'
        },
        {
            column1: 'user.name@email.com',
            column2: 'Row 4',
            column3: 'Row 4',
            date: '12-30-17',
            type: 'decline'
        },
        {
            column1: 'user.name@email.com',
            column2: 'Row 5',
            column3: 'Row 5',
            date: '11-12-18',
            type: 'decline'
        }
    ];
  }

}
