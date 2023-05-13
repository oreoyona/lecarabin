import { Component } from "@angular/core";
import { FormControl, FormGroup, Validators } from "@angular/forms";

@Component({
  selector: 'app-header-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.scss']

})
export class SearchComponent{
  searchForm = new FormGroup({
    term : new FormControl("", Validators.required)
})

  onSubmit = ()=>{
    if(this.searchForm.valid){console.log(this.searchForm.value); this.searchForm.reset()}
  }

}
