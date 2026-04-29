import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { ApiService } from './services/api.service';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet,FormsModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  question = '';
  answer = '';

  constructor(private api: ApiService) {}

  askAI() {
    this.api.ask(this.question).subscribe(res => {
      this.answer = res.answer;
    });
  }
}
