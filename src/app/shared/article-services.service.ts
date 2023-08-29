import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ArticleService {

  article = "j"

  getData1() {
    return this.http.get('./assets/articles.json');
  }

  getData2() {
    return this.http.get('./assets/images.json');
  }

  constructor(private http: HttpClient) { }
}
