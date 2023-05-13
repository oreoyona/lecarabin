import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { HomeRoutingModule } from './home-routing.module';
import { HomeComponent } from './home/home.component';
import { MainComponent } from './home/main/main.component';
import { RightSideComponent } from './home/right-side/right-side.component';
import { LeftSideComponent } from './home/left-side/left-side.component';
import { ArticleComponent } from './home/article/article.component';


@NgModule({
  declarations: [
    HomeComponent,
    MainComponent,
    RightSideComponent,
    LeftSideComponent,
    ArticleComponent
  ],
  imports: [
    CommonModule,
    HomeRoutingModule
  ]
})
export class HomeModule { }
