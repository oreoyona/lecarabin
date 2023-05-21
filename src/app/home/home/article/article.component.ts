import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-article',
  templateUrl: './article.component.html',
  styleUrls: ['./article.component.scss']
})
export class ArticleComponent implements OnInit{
  @Input() offset!: number;@Input() limit!:number; @Input() containerHeight!:number; @Input() heightVh!:number;
  screenHeight!:number;
  imageUrl = "assets/R.jpeg"


  constructor(public document: Document){

  }

  ngOnInit(): void {

  }

}
