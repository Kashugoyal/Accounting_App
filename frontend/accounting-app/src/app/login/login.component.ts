import { LoginService } from './../login.service';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router'


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

export class LoginComponent implements OnInit {

  constructor(private router:Router, private loginService: LoginService) { }

  ngOnInit() {
  }

  username :string;
  password :string;

  isLoggedIn : Boolean = false;

  login() : void 
  {
    this.loginService.login(this.username, this.password);
    if(this.loginService.isAuthenticated())
    {
      this.router.navigate[""];
    }
    else {
      alert("Invalid credentials");
    }
  }

}
