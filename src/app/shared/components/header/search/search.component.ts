import { Component } from "@angular/core";

@Component({
  selector: 'app-header-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.scss']

})
export class SearchComponent{
  value = "";
  onSubmit = ()=>{
    console.log(this.value)
  }

}
