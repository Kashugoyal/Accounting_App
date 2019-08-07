import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router'


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

export class LoginComponent implements OnInit {

  constructor(private router:Router) { }

  ngOnInit() {
  }

  username :string;
  password :string;

  isLoggedIn : Boolean = false;

  login() : void 
  {
    if(this.username == 'admin' && this.password == 'admin'){
      this.isLoggedIn = true;
      this.router.navigate([""]);
    }else {
      alert("Invalid credentials");
    }
  }

}
