import { Component, inject } from '@angular/core';
import { AuthUserService } from '../auth-user.service';
import { AuthUserComponent } from "../auth-user/auth-user.component";

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [AuthUserComponent],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {
    authUserService:AuthUserService = inject(AuthUserService)
}
