import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Router } from '@angular/router';
import { Observable, of } from 'rxjs';
import { tap } from 'rxjs/operators';
import { environment } from '../environments/environment.development';
import { Auth } from './interfaces/auth';
import { User } from './models/user.model';
// import { LocalstorageService } from './localstorage.service';

@Injectable({
  providedIn: 'root'
})
export class AuthUserService {
  public avail: boolean = false;
  public msg: string = "";

  private isAuthenticated = false;
  private redirectUrl: string | null = null;
  private authToken: string | null = null;
  private siteKey = '';
  private secretKey = '';

  private readonly TOKEN_KEY = 'token_Data';
  private readonly USER_DATA_KEY = 'USER_Data';
  private readonly SESSION_EXPIRY_KEY = 'sessionExpiryData';
  private readonly SESSION_DURATION = 5 * 24 * 60 * 60 * 1000;

  apiURLUserRegister = environment.apiUrl + 'users_file/user-registration';
  apiURLUsers = environment.apiUrl + 'users_file';
  // apiURLGoogleLogin = environment.apiUrl + 'GoogleLogin';
  // apiURLLinkedinLogin = environment.apiUrl + 'LinkedinLogin';

  constructor(
    private http: HttpClient,
    // private token: LocalstorageService,
    private router: Router
  ) { }

  // User registration methods
  createUser(user: User): Observable<User> {
    return this.http.post<User>(this.apiURLUserRegister, user);
  }

  // Login methods
  loginUser(email: string, password: string): Observable<Auth> {
    return this.http.post<Auth>(`${this.apiURLUsers}/login`, { email, password })
      .pipe(
        tap(user => {
          if (user.token) {
            this.setUserSession(user);
          }
        })
      );
  }

  // googleLogin(token: string): Observable<Auth> {
  //   return this.http.post<Auth>(`${this.apiURLGoogleLogin}/google-login`, { token })
  //     .pipe(
  //       tap(user => {
  //         if (user.token) {
  //           this.setUserSession(user);
  //         }
  //       })
  //     );
  // }

  // initiateLinkedInLogin(): void {
  //   window.location.href = `${this.apiURLLinkedinLogin}/auth/linkedin`;
  // }

  // linkedinLogin(code: string): Observable<Auth> {
  //   return this.http.get<Auth>(`${this.apiURLLinkedinLogin}/auth/linkedin/callback?code=${code}`)
  //     .pipe(
  //       tap(user => {
  //         if (user.token) {
  //           this.setUserSession(user);
  //         }
  //       })
  //     );
  // }

  // loginWithFacebook(accessToken: string, userID: string): Observable<any> {
  //   const url = `${this.apiURLUsers}/facebook-login`;
  //   const body = { accessToken, userID };
  //   return this.http.post(url, body);
  // }

  // Session management methods
  private setUserSession(user: Auth): void {
    if (user.token) {
      const data = {
        name: user.name,
        email: user.email,
        token: user.token,
        userId: user.userId,
      };
      this.authToken = user.token;
      this.setStorageItem(this.TOKEN_KEY, user.token);
      this.setStorageItem(this.USER_DATA_KEY, JSON.stringify(data));
      this.setSessionExpiry();
      this.isAuthenticated = true;

      if (user.role === undefined) {
        const redirectUrl = this.getRedirectUrl();
        this.setRedirectUrl(redirectUrl || '/user');
      }
    } else {
      console.error('User token is undefined');
      this.isAuthenticated = false;
    }
  }

  private setStorageItem(key: string, value: string): void {
    localStorage.setItem(key, value);
    sessionStorage.setItem(key, value);
  }

  private removeStorageItem(key: string): void {
    localStorage.removeItem(key);
    sessionStorage.removeItem(key);
  }

  private setSessionExpiry(): void {
    const expiryTime = new Date().getTime() + this.SESSION_DURATION;
    sessionStorage.setItem(this.SESSION_EXPIRY_KEY, expiryTime.toString());
  }

  private checkSessionExpiry(): void {
    const expiryTime = sessionStorage.getItem(this.SESSION_EXPIRY_KEY);
    if (expiryTime) {
      const currentTime = new Date().getTime();
      if (currentTime >= +expiryTime) {
        this.logout();
      }
    }
  }

  isLoggedIn(): boolean {
    this.checkSessionExpiry();
    this.authToken = this.getToken();
    return !!this.authToken;
  }

  getToken(): string | null {
    return sessionStorage.getItem(this.TOKEN_KEY) || localStorage.getItem(this.TOKEN_KEY);
  }

  logout(): void {
    this.removeStorageItem(this.TOKEN_KEY);
    this.removeStorageItem(this.USER_DATA_KEY);
    sessionStorage.removeItem(this.SESSION_EXPIRY_KEY);
    this.clearSessionStorage();
    this.isAuthenticated = false;
    this.authToken = null;
    this.router.navigate(['/login']);
  }

  private clearSessionStorage(): void {
    sessionStorage.clear();
  }

  // Password management methods
  forgotInstructorPassword(email: string): Observable<any> {
    return this.http.post(`${this.apiURLUsers}/forgot-password`, { email });
  }

  resetUserPassword(token: string, newPassword: string): Observable<any> {
    return this.http.post(`${this.apiURLUsers}/reset-password/${token}`, { newPassword });
  }

  requestPasswordReset(email: string): Observable<any> {
    return this.http.post(`${this.apiURLUsers}/forgot-password`, { email });
  }

  // Verification methods
  // verify(token: string): Observable<User> {
  //   return this.http.get(`${this.apiURLUsers}/verify/${token}`);
  // }

  verifyHcaptcha(response: string): Observable<any> {
    const requestBody = { secret: this.secretKey, response };
    return this.http.post(`${this.apiURLUsers}/verify-hcaptcha`, requestBody);
  }

  getSiteKey(): string {
    return this.siteKey;
  }

  // Redirect URL methods
  setRedirectUrl(url: string): void {
    this.redirectUrl = url;
  }

  getRedirectUrl(): string | null {
    const url = this.redirectUrl;
    this.redirectUrl = null;
    return url;
  }
}