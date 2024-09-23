import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormControl, FormGroup, ReactiveFormsModule } from '@angular/forms';

@Component({
  selector: 'app-auth-user',
  standalone: true,
  imports: [CommonModule,ReactiveFormsModule],
  templateUrl: './auth-user.component.html',
  styleUrl: './auth-user.component.css'
})
export class AuthUserComponent {
  loginForm: FormGroup = new FormGroup({
    name: new FormControl(''),
    password: new FormControl(''),
  })

  submitApplication(){

  }
}
