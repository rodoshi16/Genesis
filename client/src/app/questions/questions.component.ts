import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { MatProgressBarModule } from '@angular/material/progress-bar';
import { MatButtonModule } from '@angular/material/button';
import { HttpClient } from '@angular/common/http';
import { SpinnerComponent } from '../spinner/spinner.component';
import { ActivatedRoute } from '@angular/router';
import { switchMap } from 'rxjs';


@Component({
  selector: 'app-questions',
  standalone: true,
  imports: [MatProgressBarModule, MatButtonModule, SpinnerComponent],
  templateUrl: './questions.component.html',
  styleUrl: './questions.component.scss'
})
export class QuestionsComponent {
  questions: any = [];

  answers: String[] = []

  currentQuestion = 0;

  isLoading: boolean = false;

  constructor(private router: Router, private http: HttpClient, private route: ActivatedRoute) { }

  ngOnInit() {
    this.route.params.pipe(

      switchMap(params => {
        this.isLoading = true;
        // Extract the ID from the route parameters
        const id = params['category'];
        // Call the API with the ID
        return this.http.get(`http://localhost:8000/questions/${id}`);
      })
    ).subscribe(data => {
      this.questions = data
      this.isLoading = false;
    }, error => {
      console.error('Error fetching data:', error);
    });
  }

  answer(option: String): void {
    // Move to the next object in the list
    // If there are more objects in the list, display the next one
    this.currentQuestion++;
    this.answers.push(option);

    if (this.currentQuestion == this.questions.length) {
      console.log(this.answers);
      this.router.navigate(['/result']);
    }
  }
}
