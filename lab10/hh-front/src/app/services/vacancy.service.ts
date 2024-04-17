// vacancy.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Vacancy } from '../interfaces/vacancy.interface';

@Injectable({
  providedIn: 'root'
})
export class VacancyService {
  private apiUrl = 'http://localhost:8000/api/vacancies'; 
  
  constructor(private http: HttpClient) { }
  
  getVacancies(): Observable<Vacancy[]> {
    return this.http.get<Vacancy[]>(this.apiUrl);
  }
  
  getVacancyById(id: number): Observable<Vacancy> {
    const url = `${this.apiUrl}/${id}`;
    return this.http.get<Vacancy>(url);
  }
}
