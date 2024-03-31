import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { MatProgressBarModule } from '@angular/material/progress-bar';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'app-questions',
  standalone: true,
  imports: [MatProgressBarModule, MatButtonModule],
  templateUrl: './questions.component.html',
  styleUrl: './questions.component.scss'
})
export class QuestionsComponent {
  questions = [
    {
      question: "What is the course code for this syllabus?",
      options: [
        "APS 101",
        "APS 102",
        "APS 103",
        "APS 104"
      ],
      answer: "APS 101"
    },
    {
      question: "Who is the course coordinator?",
      options: [
        "Salma Emar",
        "Jonathan Eyolfson",
        "Bruno Korst",
        "None of the above"
      ],
      answer: "Salma Emar"
    },
    {
      question: "What is the course website?",
      options: [
        "https://www.eecg.utoronto.ca/~salma/",
        "https://eyolfson.com/",
        "https://www.ece.utoronto.ca/people/korst-b/",
        "None of the above"
      ],
      answer: "https://www.eecg.utoronto.ca/~salma/"
    },
    {
      question: "What is the course email?",
      options: [
        "salma@ece.utoronto.ca",
        "j.eyolfson@utoronto.ca",
        "bkf@ece.utoronto.ca",
        "None of the above"
      ],
      answer: "salma@ece.utoronto.ca"
    }
  ];

  answers: String[] = []

  currentQuestion = 0;

  constructor(private router: Router) { }

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
