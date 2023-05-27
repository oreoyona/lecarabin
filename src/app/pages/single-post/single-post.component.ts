import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-single-post',
  templateUrl: './single-post.component.html',
  styleUrls: ['./single-post.component.scss']
})
export class SinglePostComponent implements OnInit{
  date!: string
  ngOnInit(): void {
    const laDate = new Date();
    const maintenant = laDate.toUTCString()
    this.date = `${laDate.toLocaleDateString()}`
  }






}
