export interface EventModel {
  id: number;
  title: string;
  organizers: number[];
  members: number[];
  school: string;
  school_id: number;
  teams: EventTeam[];
  description: string;
  created_at: string;
}

export interface EventTeam {
  team: number;
  members: number[];
}
