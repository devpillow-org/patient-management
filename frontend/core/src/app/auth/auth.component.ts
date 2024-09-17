import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms'; // <-- NgModel lives here

import { User } from './user';

@Component({
  selector: 'app-auth',
  standalone: true,
  imports: [],
  templateUrl: './auth.component.html',
  styleUrl: './auth.component.css'
})
export class AuthComponent {
  userData: User = {
    name: '',
    password: ''
  }

  submitForm(form: any): void {
    if (form.valid) {
      console.log('Form data:', this.userData);
    }
  }
}
