import { Component, Input, OnInit } from '@angular/core';
import { ArticleService } from 'src/app/shared/article-services.service';

@Component({
  selector: 'app-article',
  templateUrl: './article.component.html',
  styleUrls: ['./article.component.scss']
})
export class ArticleComponent implements OnInit{
  @Input() offset!: number;@Input() limit!:number; @Input() containerHeight!:number; @Input() heightVh!:number;
  screenHeight!:number;
  @Input() headerSize!:number;@Input() headerSizeRem!:number;

  articles = [];
  images: any


  constructor(public document: Document, private articleService: ArticleService){

  }

  ngOnInit() {
    const data1 = this.articleService.getData1();
    const data2 = this.articleService.getData2();

    data2.subscribe((items:any) => {this.images = items})

  }

}
