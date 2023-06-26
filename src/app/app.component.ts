import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})

export class AppComponent implements OnInit{
  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin':'*'
    })
  };
  title = 'lecarabin';
  onLoad(){
    this.http.get('localhost:5000/api/articles', this.httpOptions).subscribe((e)=>{
      console.log(e)
    })
  }

  constructor(private http: HttpClient){}

  ngOnInit(): void {
    this.onLoad()

  }


}
