import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient, HttpClientModule } from '@angular/common/http';

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
    HomeRoutingModule,
    HttpClientModule
  ],
  providers: [{provide: HttpClient, useClass: HttpClient}]
})
export class HomeModule { }
