import { Component, OnInit } from '@angular/core';
import { ArticleService } from 'src/app/shared/article-services.service';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.scss']
})
export class MainComponent{
  offset = 1;
  limit = 2;
  imageUrl = "./assets/R.jpeg";

  grid_4_article = [];



  constructor(private articleService: ArticleService){}
}
