import { HttpService } from './../http.service';
import { Component, OnInit } from '@angular/core';
import {User} from '../app-classes';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-app-dashboard',
  templateUrl: './app-dashboard.component.html',
  styleUrls: ['./app-dashboard.component.css']
})
export class AppDashboardComponent implements OnInit {

  constructor(private http : HttpService) { }

  users:any;
  selected_user:any;
  ngOnInit()
  {
    this.http.get_users()
      .subscribe(data=> 
        {
          this.users = data; 
          console.log(this.users);
        });
  }

  onSelect(user)
  {
    this.selected_user = user;
    console.log(this.selected_user);
  }
}
